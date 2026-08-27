class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "uai"
        return '_uai_'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'uai':
            return []
        return s.split('_uai_')
