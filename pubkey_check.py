def is_valid_pubkey(pubkey):
    # Public keys are usually 64-char hex strings
    return len(pubkey) == 64 and all(c in '0123456789abcdefABCDEF' for c in pubkey)

sample_key = "a" * 64
print(f"Valid Public Key Format: {is_valid_pubkey(sample_key)}")
