from django import  forms
class OrganizationForm(forms.Form):
    org_id = forms.IntegerField(max_value=99999,label="Organization Id",min_value=10000)
    org_name = forms.CharField(max_length=30,label="Organization Name")
    org_address = forms.CharField(max_length=60,label="Organization Address")
    org_country = forms.CharField(max_length=30,label="Country")
    gropus = [("India", "America", "Australia"), ("it", "Information")]
    org_state = forms.CharField(max_length=20,label="State")
    org_city = forms.CharField(max_length=20,label="City")
    org_email = forms.EmailField(max_length=50,label="Email Id")
    org_password = forms.CharField(max_length=8,widget=forms.PasswordInput,min_length=8,label="Password")
    org_contact = forms.IntegerField(max_value=9999999999,label="Contact No")




