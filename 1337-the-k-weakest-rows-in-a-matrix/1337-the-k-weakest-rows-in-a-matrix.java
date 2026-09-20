class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        List<Integer> ans = new ArrayList<>();
        List<Integer> lst = new ArrayList<>();
        for(int i = 0 ; i < mat.length ; i++){
            int c = 0;
            for(int j = 0 ; j < mat[0].length ; j++){
                if (mat[i][j] == 1){
                    c += 1;
                }
            }ans.add(c);
        }
        for(int i = 0 ; i < ans.size() ; i++){
            int a = Integer.MAX_VALUE;
            int index = -1;
            for(int j = 0 ; j < ans.size() ; j++){
                if (ans.get(j) < a){
                    a = ans.get(j);
                    index = j;
                }
            }
            lst.add(index);
            ans.set(index, Integer.MAX_VALUE);
        }
        int[] result = new int[k];
        for(int m = 0 ; m < k ; m++){
            result[m] = lst.get(m);
        }
        return result;
    }
}