from django import forms
from .models import Wallet

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ["owner", "starting_stock"]
    
    def is_valid(self) -> bool:
        print("\n\t data-wallet-forms: ", self.data)
        data = self.data
        owner = data['owner']
        starting_stock = data['starting_stock']
        self.cleaned_data = {
            "starting_stock": starting_stock,
            "owner": owner,
        }
        return True