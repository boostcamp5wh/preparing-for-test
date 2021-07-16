package kakaoBlind2021._07_매출하락최소화;

import java.util.*;

public class Solution {
    Map<Integer,ArrayList<Integer>> tree;
    int[] sales;
    int[][] dp;
    int[] sum_child;
    public int solution(int[] sales, int[][] links) {
        int answer = 0;
        this.sales = sales;
        tree = new HashMap<>();
        this.dp=new int[sales.length+1][2];
        this.sum_child = new int[sales.length+1];
        for(int link[]:links){
            int p = link[0];
            int c = link[1];
            
            ArrayList<Integer> arr = tree.getOrDefault(p,new ArrayList<>());
            arr.add(c);

            tree.put(p,arr);
        }
        dfs(1);
        return Math.min(dp[1][0],dp[1][1]);
    }
    
    public void dfs(int i){
        
        ArrayList<Integer> list = this.tree.getOrDefault(i, new ArrayList<>());
        
        if(list.isEmpty())
        {
            dp[i][1]=sales[i-1];
            return;
        }
        boolean flag=false;
        int min = Integer.MAX_VALUE;
        for(int k : list){
            dfs(k);
            sum_child[i]+=Math.min(dp[k][0],dp[k][1]);
            min = Math.min(min,dp[k][1]-dp[k][0]);
            if(dp[k][0]>dp[k][1])
                flag=true;
        }
       
        dp[i][1] = sales[i-1]+sum_child[i];
        if(flag){
            dp[i][0] = sum_child[i];
        }else{
            dp[i][0] = sum_child[i]+min;
        }
        
    }
    
}
