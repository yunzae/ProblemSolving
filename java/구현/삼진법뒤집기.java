package 구현;

import java.util.*;
class 삼진법뒤집기 {
    public int 삼진법뒤집기(int n) {
        String n3 = Integer.toString(n,3);

        StringBuilder sb = new StringBuilder(n3);
        sb.reverse();
        return Integer.parseInt(sb.toString(),3);

    }
}
