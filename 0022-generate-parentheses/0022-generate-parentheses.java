class Solution {
    ArrayList<String> r = new ArrayList<>();
    public List<String> generateParenthesis(int n) {  
        g("" , 0 , 0 , n);
        return r;
    }

    void g(String s , int o , int c , int n){
            if(s.length() == 2 * n){
                r.add(s);
            }
            if(o < n){
                g(s + "(" , o + 1 , c , n);
            }
            if(c < o){
                g(s + ")" , o , c + 1 , n);
            }
        }
    }
        