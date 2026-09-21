class Solution {
    List<List<String>> ans = new ArrayList<>();
    public List<List<String>> partition(String s) {
        b(s , 0 , new ArrayList<>());
        return ans;
    }
    void b(String s , int start , List<String> path){
        if (start == s.length()){
            ans.add(new ArrayList<>(path));
        }
        for(int i = start ; i < s.length() ; i++){
            String part = s.substring(start , i+1);
            if(part.equals(new StringBuilder(part).reverse().toString())){
                path.add(part);
                b(s , i+1 , path);
                path.remove(path.size()-1);
            }
        }
    }
}