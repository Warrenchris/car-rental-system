import java.io.Serializable;

public class Person implements Serializable {
    private String firstName;
    private String lastName;
    private String email;
    private String phoneNo;
    private String IDNO;


    public Person() {
    }

    public Person(String firstName, String lastName, String email, String phoneNo, String IDNO) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.phoneNo = phoneNo;
        this.IDNO=IDNO;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhoneNo() {
        return this.phoneNo;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public String getIDNO() {
        return IDNO;
    }

    public void setIDNO(String IDNO) {
        IDNO = IDNO;
    }

    @Override
    public String toString() {
        return 
            "First Name = " + getFirstName() + "\n" +
            "Last Name = " + getLastName() + "\n" +
            "Email = " + getEmail() + "\n" +
            "Phone No = " + getPhoneNo() + "\n"+
            "IDNO = " + getIDNO() + "\n";
    }


}
