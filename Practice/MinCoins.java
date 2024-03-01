import java.util.Scanner;

public class MinCoins {
    public static int minCoins(int n) {
        int[] coins = {1, 3, 6, 10, 15};
        int[] minCoins = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            minCoins[i] = Integer.MAX_VALUE;
            for (int coin : coins) {
                if (i - coin >= 0) {
                    minCoins[i] = Math.min(minCoins[i], minCoins[i - coin] + 1);
                }
            }
        }

        return minCoins[n];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            System.out.println(minCoins(n));
        }
        scanner.close();
    }
}
