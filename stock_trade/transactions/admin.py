from email.headerregistry import Group
from typing import Any, Dict, Optional
from django.contrib import admin
from .forms import WalletForm
from datetime import datetime

from django.contrib.auth.models import Group
from django.http.request import HttpRequest
from django.http.response import HttpResponse
import logging
from .models import (
    Transactions,
    Wallet
)
from django.contrib import messages
from django.contrib.auth import get_user_model
Users = get_user_model()


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ["wallet_owner", "transaction_date", "amount"]
    list_filter = ["wallet_id"]


    



class WalletAdmin(admin.ModelAdmin):
    list_display = ["wallet_owner", "starting_stock", "date_created"]
    list_filter = ["owner"]
    add_form = WalletForm


    def add_view(self, request: HttpRequest, form_url="", extra_context={}) -> HttpResponse:
        try:
            if request.method == "POST":
                super().add_view(request, form_url, extra_context)
                form = WalletForm(request.POST)
                if form.is_valid():
                    cleaned_data = form.cleaned_data
                    wallet_owner = Users.objects.filter(pk=cleaned_data['owner'])
                    wallet_exists = Wallet.objects.filter(owner=wallet_owner[0])
                    print("\n\t wallet_exists: ", wallet_exists[0])
                    if not wallet_exists:
                        print("\n\t wallet_owner: ", wallet_owner[0])
                        logging.info("Creating a new wallet...")
                        string_date = datetime.now().date().strftime("%c").split(" ")
                        new_wall = Wallet()
                        new_wall.starting_stock = cleaned_data["starting_stock"]
                        new_wall.owner = wallet_owner[0]
                        new_wall.string_date = f"{string_date[0]} {string_date[1]} {string_date[2]} {string_date[4]}"
                        new_wall.save()
                        return super().add_view(request)
                    messages.set_level(request, messages.ERROR)
                    self.message_user(request, "This user has a wallet already.", messages.ERROR)
                    return (request, form_url, extra_context)
                raise form.errors
            else:
                return super().add_view(request, form_url, extra_context)
        except Exception as err:
            print("\n\t Errrr: ", err)
            print("\n\t Req: ", request)
        return super().add_view(request, form_url, extra_context)




        # return super().save_model(request, obj, form, change)


    



admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Wallet, WalletAdmin)


