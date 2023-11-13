class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i =left;i<=right;i++){
            int n = 0;
            for (int j=1;j<=i;j++){
                if(i%j==0){
                    n+=1;
                }
            }
            if (n%2==0){
                System.out.println("+");
                System.out.println(i);
                answer+=i;
            }else{
                System.out.println("-");
                System.out.println(i);
                answer-=i;
            }
        }

        return answer;
    }
}