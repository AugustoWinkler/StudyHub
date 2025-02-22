package leetcode.metods;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class L0028_FindtheIndexoftheFirstOccurrenceinaString {

	public int strStr(String haystack, String needle) {
		Pattern pattern = Pattern.compile(needle);
		Matcher matcher = pattern.matcher(haystack);

		if (!matcher.find()) {
			return -1;
		}
		return matcher.start();
	}
}
