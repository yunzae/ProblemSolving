package 구현;

class 비밀지도 {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for( int i =0; i<n; i++){
            int[] temp1 = to2(n, arr1[i]);
            int[] temp2 = to2(n, arr2[i]);
            StringBuilder sb = new StringBuilder();
            for(int j=0; j<n; j++){
                if(temp1[j]==0 && temp2[j]==0){
                    sb.append(" ");
                }else{
                    sb.append("#");
                }
            }
            answer[i] = sb.toString();
        }

        return answer;
    }

    public static int[] to2(int n, int num){
        int[] temp = new int[n];
        for(int i=0; i < n; i++){
            temp[i] = num/(int)Math.pow(2,n-i-1);
            num= num%(int)Math.pow(2,n-i-1);
        }
        return temp;
    }
}