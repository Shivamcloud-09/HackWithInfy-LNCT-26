class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        List <Integer> ans = new ArrayList<>();
        for(int i = 0 ; i < matrix.length ; i++){
            int min = matrix[i][0];
            int a = 0 ; 
            for(int j = 0 ; j < matrix[0].length ; j++){
                if(matrix[i][j] < min){
                    min = matrix[i][j];
                    a = j;
                }
            }
            boolean b = true;
            for(int k = 0 ; k < matrix.length ; k++){
                if(matrix[k][a] > min){
                    b = false;
                    break;
                }
            }
            if(b){
                ans.add(min);
            }}
        return ans;
    }
}