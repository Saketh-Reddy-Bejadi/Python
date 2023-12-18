import java.util.Scanner;

public class gameAndMultiset {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int testCases = scanner.nextInt();
        scanner.nextLine(); 

        for (int t = 0; t < testCases; t++) {
            String q = scanner.nextLine().trim();
            int p = countOccurrences(q, '0');
            int z = countOccurrences(q, '1');
            StringBuilder ans = new StringBuilder();

            for (int i = 0; i < q.length(); i++) {
                if (q.charAt(i) == '0' && z < 1) break;
                if (q.charAt(i) == '1' && p < 1) break;
                if (q.charAt(i) == '0' && z > 0) {
                    ans.append('1');
                    z--;
                } else if (q.charAt(i) == '1' && p > 0) {
                    ans.append('0');
                    p--;
                }
            }

            System.out.println(Math.abs(q.length() - ans.length()));
        }
        scanner.close();
    }

    private static int countOccurrences(String str, char target) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == target) {
                count++;
            }
        }
        return count;
        
    }

}