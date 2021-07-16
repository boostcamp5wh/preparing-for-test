package kakaoBlind2021._01_아이디추천;

public class Solution {
    public String solution(String new_id) {
        
        new_id = new_id.toLowerCase();
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<new_id.length();i++){
            char ch = new_id.charAt(i);
            
            if((ch>='a'&& ch<='z') || 
               (ch>='0'&&ch<='9')
               || ch=='_' || ch=='.'||ch=='-')
                sb.append(ch);
            
        }
        new_id=sb.toString();
        
        while(new_id.contains("..")){
            new_id=new_id.replace("..",".");
        }
        
        if(new_id.length()>0 && new_id.charAt(0)=='.')
            new_id=new_id.substring(1);
        if(new_id.length()>0 && new_id.charAt(new_id.length()-1)=='.')
            new_id=new_id.substring(0,new_id.length()-1);
        if(new_id.equals(""))
            new_id="a";
        if(new_id.length()>=16)
            new_id=new_id.substring(0,15);
        if(new_id.charAt(new_id.length()-1)=='.')
            new_id=new_id.substring(0,new_id.length()-1);
        
        if(new_id.length()<=2){
            char f = new_id.charAt(new_id.length()-1);
            while(new_id.length()<=2){
                new_id+=f;
            }
            
        }
        
        return new_id;
    }
}