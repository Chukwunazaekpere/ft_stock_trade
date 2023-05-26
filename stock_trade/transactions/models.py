from typing import Iterable, Optional
from django.db import models
# from dja
from django.conf import settings
from datetime import datetime
from django.contrib.auth import get_user_model
import logging
Users = get_user_model()

logging.basicConfig(level=logging.INFO)


class Wallet(models.Model):
    owner = models.OneToOneField(Users, on_delete=models.CASCADE)
    starting_stock = models.DecimalField(max_digits=18, decimal_places=2)
    string_date = models.CharField(max_length=35, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

 
    def wallet_owner(self):
        return f"{self.owner}"

    def __str__(self) -> str:
        return f"{self.owner}"

    # def save(self, **kwargs) -> None:
    #     try:
    #         print("\n\t KWARGS: ", kwargs)
    #         logging.info("Creating a new wallet...")
    #         self.string_date = datetime.now().date().strftime("%c")
    #         self.save(**kwargs)
    #         logging.info("Wallet was sucessfully created...")
    #         return super().save()
    #     except Exception as save_wallet_error:
    #         print("\n\t wallet_exception: ", save_wallet_error)
    #         return False
    # # def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
    # #     return super().save(force_insert, force_update, using, update_fields)

        
        
    class Meta:
        verbose_name_plural = "Wallets"
        verbose_name = "Wallet"



class Transactions(models.Model):
    wallet_id = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    string_date = models.CharField(max_length=35, editable=False)
    transaction_date = models.DateTimeField(verbose_name="Date of Registration", auto_now_add=True)

 

    def wallet_owner(self):
        return f"{self.wallet_id}"

    def __str__(self) -> str:
        return f"{self.wallet_id}"
        
        
    class Meta:
        verbose_name_plural = "Transactions"
        verbose_name = "Transaction"


