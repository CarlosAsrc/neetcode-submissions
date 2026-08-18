class Solution {
    public int[] countBits(int n) {
        int res[] = new int[n+1];
        for(int i=0; i<=n; i++) {
            res[i] = countBitsForNht(i);
        }
        return res;
    }
    
    public int countBitsForNht(int nht){
        int res = 0;
        while (nht != 0) {
            res = res + (nht & 1);
            nht = nht >> 1;
        }
        return res;
    }
}
