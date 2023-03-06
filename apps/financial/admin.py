from admin_site import admin
from apps.financial.models import SellerCommissionPayment, RoyaltiesPayment


@admin.register(SellerCommissionPayment)
class SellerCommissionPaymentAdmin(admin.ModelAdmin):
    list_display = ('status', 'order_id', 'order_customer', 'order_created_at')

    def order_id(self, obj):
        return obj.order.id

    def order_customer(self, obj):
        return obj.order.id

    def order_created_at(self, obj):
        return obj.order.id

@admin.register(RoyaltiesPayment)
class RoyaltiesPaymentAdmin(admin.ModelAdmin):
    list_display = ('status', 'order_id', 'order_customer', 'order_created_at')

    def order_id(self, obj):
        return obj.order.id

    def order_customer(self, obj):
        return obj.order.id

    def order_created_at(self, obj):
        return obj.order.id