class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = "".join(strs)
        lengths = ''
        for string in strs:
            lengths += ' ' + str(len(string))
        return lengths + '\t' + encodedStr
    
    def decode(self, s: str) -> List[str]:
        lengths = s.split("\t")[0]
        lengths = lengths.split(' ')
        strs = '\t'.join((s.split("\t")[1:]))
        decodedStrs = []
        for stringLength in lengths:
            if stringLength == '':
                continue
            decodedStrs.append(strs[0:int(stringLength)])
            strs = strs[int(stringLength):]
        return decodedStrs