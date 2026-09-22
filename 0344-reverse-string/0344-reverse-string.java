class Solution {
    public void reverseString(char[] s) {
        for(int i = 0 ; i < s.length/2 ; i++){
            int n = s.length - 1 - i ;
            char temp = s[i];
            s[i] = s[n];
            s[n] = temp;
        }
    }
        
}