class Solution {
    public void rotate(int[][] matrix) {
        int n  = matrix.length ;
        int lst[][] = new int[n][n];
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < n ; j++){
                lst[j][n - 1 - i] = matrix[i][j];
            }
        }
        for(int i = 0 ; i < n ; i++){
            System.arraycopy(lst[i] , 0 , matrix[i] , 0 , n);
        }
    }
}