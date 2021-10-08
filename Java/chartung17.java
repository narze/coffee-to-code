import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class chartung17 {
	public static void main(String[] args) {
		String coffee = "Coffee";
		Set<Character> set = new TreeSet<>(
				(a, b) -> (int) Math.signum(Math.abs(105.4 - b) - Math.abs(105.4 - a)));
		coffee.chars().mapToObj(a -> a).collect(Collectors.toMap(a -> a, a -> 1, (a, b) -> a + b))
				.forEach((k, v) -> set.add((char) (k - v + 1)));
		StringBuilder sb = new StringBuilder();
		for (char c : set) {
			sb.append(c);
		}
		System.out.println(sb);
	}
}
