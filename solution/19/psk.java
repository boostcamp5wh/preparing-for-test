package kakaoBlind2020._01_문자열압축;

class Solution {
    public static int solution(String s) {
        
        int len = s.length();
        int answer = len;
        
        for(int i=1;i<=len/2;i++){//쪼갤 개수 정하기
            String unit = s.substring(0,i);//첫 단위
            int cnt=0;//단위 별 카운트
            String result="";
            
            for(int j=0;j<=len;j=j+i){
            	
//                System.out.println("확인 : "+unit);
//                System.out.println("확인 : "+j);
                if(s.indexOf(unit,j)==j){
                    cnt++;
                    
                }
               else if(s.indexOf(unit,j)!=j){
                   
                   if(cnt>=2){
                       result = result+cnt+unit;
                   }else if(cnt<=1){
                        result = result+unit;
                   }
                   
                   cnt=1;
                   if(j+i>s.length()){
                       unit = s.substring(j,j+s.length()%i);
                       result = result+unit;
                       
                   }else{
                       unit = s.substring(j,j+i);
                   }
                   
                   
               }
                
            }
            answer = Math.min(answer, result.length());
//            System.out.println(result);
        }
        return answer;
    }
}
