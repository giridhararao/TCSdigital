import java.util.*;

public class Main{
    
    public static String getprefix(ArrayList<String> a){
        String s="";
        int i=0;
        int minl=10000000;
        for(String si:a){
            if(si.length()<minl){
                minl=si.length();
            }
        }
        while(i<minl){
            if((a.get(0).charAt(i)==a.get(1).charAt(i)) &&(a.get(0).charAt(i)==a.get(2).charAt(i))){
                s=s+(a.get(0).charAt(i));
                i++;
            }
            else{
                break;
            }
        }
        return(s);
    }
    
    public static void main(String[] args){
        ArrayList<String> a=new ArrayList<String>();
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<3;i++){
            String s=sc.nextLine();
            a.add(s);
        }
        System.out.println(getprefix(a));
        
    }
}
