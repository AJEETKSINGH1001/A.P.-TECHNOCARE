from decimal import Decimal, ROUND_HALF_UP


MONEY_PLACES = Decimal("0.01")


def money(value):
    """
    Convert a value to Decimal and round it to 2 decimal places.
    """
    return Decimal(value).quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


def calculate_quotation_totals(
    items,
    discount=Decimal("0.00"),
    supply_type="intra_state",
):
    """
    Calculate quotation totals from quotation items.

    Each item must provide:
        quantity
        unit_price
        gst_rate

    supply_type:
        intra_state -> CGST + SGST
        inter_state -> IGST

    Returns a dictionary containing:
        subtotal
        discount
        taxable_amount
        cgst
        sgst
        igst
        grand_total
    """

    subtotal = Decimal("0.00")
    cgst = Decimal("0.00")
    sgst = Decimal("0.00")
    igst = Decimal("0.00")

    for item in items:
        quantity = Decimal(str(item.quantity))
        unit_price = Decimal(str(item.unit_price))
        gst_rate = Decimal(str(item.gst_rate))

        line_taxable = money(quantity * unit_price)
        subtotal += line_taxable

        if supply_type == "inter_state":
            line_igst = money(line_taxable * gst_rate / Decimal("100"))
            igst += line_igst

        else:
            total_gst = money(line_taxable * gst_rate / Decimal("100"))

            line_cgst = money(total_gst / Decimal("2"))
            line_sgst = total_gst - line_cgst

            cgst += line_cgst
            sgst += line_sgst

    subtotal = money(subtotal)
    discount = money(discount)

    if discount < Decimal("0.00"):
        raise ValueError("Discount cannot be negative.")

    if discount > subtotal:
        raise ValueError("Discount cannot be greater than subtotal.")

    taxable_amount = money(subtotal - discount)

    # GST should be calculated on the discounted taxable amount.
    # Recalculate tax when a discount is applied.
    cgst = Decimal("0.00")
    sgst = Decimal("0.00")
    igst = Decimal("0.00")

    if taxable_amount > Decimal("0.00") and subtotal > Decimal("0.00"):
        discount_ratio = taxable_amount / subtotal

        for item in items:
            quantity = Decimal(str(item.quantity))
            unit_price = Decimal(str(item.unit_price))
            gst_rate = Decimal(str(item.gst_rate))

            original_line_value = money(quantity * unit_price)
            discounted_line_value = money(
                original_line_value * discount_ratio
            )

            if supply_type == "inter_state":
                igst += money(
                    discounted_line_value
                    * gst_rate
                    / Decimal("100")
                )
            else:
                total_gst = money(
                    discounted_line_value
                    * gst_rate
                    / Decimal("100")
                )

                line_cgst = money(total_gst / Decimal("2"))
                line_sgst = total_gst - line_cgst

                cgst += line_cgst
                sgst += line_sgst

    cgst = money(cgst)
    sgst = money(sgst)
    igst = money(igst)

    grand_total = money(
        taxable_amount + cgst + sgst + igst
    )

    return {
        "subtotal": subtotal,
        "discount": discount,
        "taxable_amount": taxable_amount,
        "cgst": cgst,
        "sgst": sgst,
        "igst": igst,
        "grand_total": grand_total,
    }