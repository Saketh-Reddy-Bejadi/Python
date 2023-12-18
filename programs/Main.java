import java.util.*;

public class Main {
    static final int MOD = 998244353;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] p = new int[n];
            for (int i = 0; i < n; i++) {
                p[i] = sc.nextInt(); 
            }
            
            long ways = 1;
            for (int i = 1; i < n; i++) {
                int smaller = 0;
                for (int j = 0; j < i; j++) {
                    if (p[j] < p[i]) {
                        smaller++;
                    }
                }
                ways = (ways * (smaller + 1)) % MOD; 
            }
            
            System.out.println(ways);
        }
        
        sc.close();
    }
}