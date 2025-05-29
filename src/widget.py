def mask_account_card(x: str):
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if 'счет' in x.lower():
        mask_account_card_ = x[:4] + ' ' + '**' + x[-4:]
        return mask_account_card_

    else:
        for i, j in zip(x, range(len(x))):
            if i.isdigit():
                card_number_ = x[j:]
                mask_account_card_ = x[:4] + ' ' + card_number_[:4] + " " + card_number_[4:6] + "**" + " " + "****" + " " + card_number_[12:]
                return mask_account_card_

print(mask_account_card('Visa 339933933939'))