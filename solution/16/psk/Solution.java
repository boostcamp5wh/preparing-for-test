package Programmers.kakaoBLIND2021.순위검색;

import java.util.*;
class Solution {
    
    public String makeKey(String... args){
        StringBuilder sb = new StringBuilder();
        // String s="";
        for(int i=0;i<args.length;i++){
            sb.append(args[i]);
            sb.append(" ");
            // s+=args[i]+" ";
        }
        return sb.toString().trim();
        // return s.trim();
    }
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        Map<String,ArrayList<Integer>> map = new HashMap<>();
        
    String lang[]={"cpp","java","python"};
    String job[]={"backend","frontend"};
    String career[]={"junior","senior"};
    String soul[]={"chicken","pizza"};
        
        for(String i : lang)
            for(String j : job)
                for(String k:career)
                    for(String l:soul)
                    {
                        String key = makeKey(i,j,k,l);
                        map.put(key,new ArrayList<>());
                    }
        for(String ele : info){
           String[] tmp=ele.split(" ");
           String key=makeKey(tmp[0],tmp[1],tmp[2],tmp[3]);
           ArrayList<Integer> arr = map.getOrDefault(key,
                                                    new ArrayList<>());
            arr.add(Integer.parseInt(tmp[4]));
            Collections.sort(arr);
            
        }
        int idx=0;
        for(String q:query){
            String tmp[]=q.split(" ");
            int score = Integer.parseInt(tmp[7]);
            String[] a,b,c,d;
            if(tmp[0].equals("-"))
                a=lang;
            else
                a=new String[]{tmp[0]};
            if(tmp[2].equals("-"))
                b=job;
            else
                b=new String[]{tmp[2]};
            if(tmp[4].equals("-"))
                c=career;
            else
                c=new String[]{tmp[4]};
            if(tmp[6].equals("-"))
                d=soul;
            else
                d=new String[]{tmp[6]};
            int cnt=0;
            
            for(String i :a)
                for(String j :b)
                    for(String k :c)
                        for(String l :d){
                            String key=makeKey(i,j,k,l);
                            ArrayList<Integer> arr
                                =map.getOrDefault(key,new ArrayList<>());
                            int left=0,right=arr.size()-1,mid=0;
                            while(left<=right){
                                mid=(left+right)/2;
                                if(arr.get(mid)>=score)
                                    right=mid-1;
                                else
                                    left=mid+1;
                            }
                            cnt+=arr.size()-right-1;
                        }
            
            answer[idx++]=cnt;
        }
        
        return answer;
    }
}
