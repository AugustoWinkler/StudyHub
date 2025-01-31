package leetcode.metods;

public class L0020_ValidParentheses {

	public boolean isValid(String s) {
		while (s.contains("()") | s.contains("[]") | s.contains("{}")) {
			s = s.replaceAll("\\(\\)", "");
			s = s.replaceAll("\\{\\}", "");
			s = s.replaceAll("\\[\\]", "");
		}
		if (s.length() > 0)
			return false;
		return true;
	}

}
