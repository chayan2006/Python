import hashlib
import os
from . import config, voice

class Authenticator:
    def __init__(self):
        self.owner_name = config.OWNER_NAME
        self.voice = voice.VoiceEngine()

    def is_configured(self):
        """Checks if a voice key has been set."""
        return os.path.exists(config.VOICE_KEY_FILE)

    def set_voice_key(self, phrase):
        """Saves the voice key phrase."""
        with open(config.VOICE_KEY_FILE, 'w') as f:
            f.write(phrase)

    def get_voice_key(self):
        """Retrieves the voice key phrase."""
        if not self.is_configured():
            return config.SECRET_PHRASE # Fallback
        with open(config.VOICE_KEY_FILE, 'r') as f:
            return f.read().strip()

    def _hash_phrase(self, phrase):
        return hashlib.sha256(phrase.encode()).hexdigest()

    def verify_voice_phrase(self, input_phrase):
        """
        Verifies the spoken secret phrase.
        """
        target_phrase = self.get_voice_key()
        
        # Normalize for case and punctuation
        cleaned_input = input_phrase.lower().strip(".,!?")
        cleaned_secret = target_phrase.lower().strip(".,!?")
        
        # Simple containment check for robustness
        if cleaned_secret in cleaned_input:
            return True
            
        # Fuzzy match (handle slight misinterpretations)
        from difflib import SequenceMatcher
        similarity = SequenceMatcher(None, cleaned_secret, cleaned_input).ratio()
        if similarity > 0.7: # 70% match is enough
            return True

        return False

    def verify_token(self, token):
        """
        Verifies a session token.
        """
        # Mock implementation
        return token == "valid_token_123"

    def authenticate(self, user_input, token=None):
        """
        Main authentication entry point.
        """
        if token and self.verify_token(token):
            return True
        
        if self.verify_voice_phrase(user_input):
            return True
            
        return False

    def authenticate_voice(self):
        """
        Captures voice and attempts authentication.
        """
        self.voice.speak("Identify yourself.")
        phrase = self.voice.listen()
        if phrase:
            return self.authenticate(phrase), phrase
        return False, None
