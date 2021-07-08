package Programmers.kakaoBLIND2021.메뉴리뉴얼;

import java.util.*;
class Solution {
    
    Map<String,Integer> map  = new TreeMap<>();
    public String[] solution(String[] orders, int[] course) {
        String[] answer = {};

        for(int i=0;i<orders.length;i++){
            char tmp[] = orders[i].toCharArray();
            Arrays.sort(tmp);
            orders[i]=new String(tmp);
            bit(tmp,tmp.length,i);
        }
        
        Set<String> tmp_set = new HashSet<>(map.keySet());
        
        for(String str : tmp_set){
            if(map.get(str)<2)
                map.remove(str);
        }
        
        Set<String> ret = new TreeSet<>();
        
        for(int cnt:course){
            
            int max=0;
            
            for(String str : map.keySet()){
                if(str.length()==cnt){
                    max=Math.max(max,map.get(str));
                }
            }
            
            for(String str : map.keySet()){
                if(str.length()==cnt&&map.get(str)==max)
                    ret.add(str);
            }
        }
        
        
        return ret.toArray(new String[0]);
    }
    
    public String[] bit(char[] arr, int n, int idx) {
    List<String> list = new ArrayList<>();
  
    for(int i=0; i < 1<<n; i++) {
        StringBuilder sb  =new StringBuilder();
        for(int j=0; j<n; j++) {
            if((i & 1<<j) != 0) 
                sb.append(arr[j]);
        }
        if(sb.length()>=2){
            String tmp = sb.toString();
            map.put(tmp,map.getOrDefault(tmp,0)+1);
        }
        
        
    }
        return list.toArray(new String[0]);
    }
    
}