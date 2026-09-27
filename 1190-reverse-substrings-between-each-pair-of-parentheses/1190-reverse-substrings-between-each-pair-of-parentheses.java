class Solution {
    public String reverseParentheses(String s) {
        List<Character> lst = new ArrayList<>();
        for(char i : s.toCharArray()){
            if (i == ')'){
                String st = "";
                while (lst.get(lst.size() -1) != '('){
                    st += lst.remove(lst.size() -1);
                }
                lst.remove(lst.size()-1);
                for(char j : st.toCharArray()){
                    lst.add(j);
                }
            }
            else{
                lst.add(i);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(char k : lst){
            sb.append(k);
        }
        return sb.toString();
    }
}