class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        
        for(int i = 0 ; i < image.length ; i++){
            int n = image[i].length;
            for(int j = 0 ; j < n / 2 ; j++){
                int t = n - 1 - j ;
                int temp = image[i][j];
                image[i][j] = image[i][t];
                image[i][t] = temp;
            }
        }
        for(int i = 0 ; i < image.length ; i++){
            for(int j = 0 ; j < image[0].length ; j++){
                if(image[i][j] == 1){
                    image[i][j] = 0;
                }
                else{
                    image[i][j] = 1;
                }
            }
        }
        return image;
    }
}