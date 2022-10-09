import java.util.List;

public class Kanoonsantikul {

	private static class Person {
		public String eat(Object input) {
			return "Poop";
		}
	}

	private static class Programmer extends Person {
		@Override
		public String eat(Object input) {
			if (input.getClass().getSimpleName().equals("Coffee")) {
				return "Code";
			} else {
				return super.eat(input);
			}
		}
	}

	private static class Coffee {}

	public static void main(String[] args) {
		Programmer bob = new Programmer();
		List<Object> menuList = List.of("0xDEADBEEF", false, 100_000_000, new Coffee());
		for (Object menu : menuList) {
			System.out.println("What happen if programmer eat " + menu.getClass().getSimpleName());
			System.out.println("It is " + bob.eat(menu) + "!!");
		}
	}

}