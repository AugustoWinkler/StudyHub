package leetcode.metods;

public class L1108_DefangingAnIpAddress {

	public String defangIPaddr(String address) {
        String defangedIp = address.replace(".", "[.]");
        return defangedIp;
    }
}
