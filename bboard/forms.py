from django import forms

class AddAdvancedProductForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название товара", widget=forms.TextInput(attrs={'placeholder': 'Например: Игровой ПК'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Цена (руб.)")
    
    # Поля, которые мы потом упакуем в один JSON-объект
    brand = forms.CharField(max_length=50, label="Бренд", widget=forms.TextInput(attrs={'placeholder': 'Asus, HP...'}))
    cpu = forms.CharField(max_length=100, label="Процессор", widget=forms.TextInput(attrs={'placeholder': 'Intel i5, Ryzen 5...'}))
    ram = forms.CharField(max_length=50, label="Оперативная память", widget=forms.TextInput(attrs={'placeholder': '16 ГБ, 32 ГБ...'}))
    gpu = forms.CharField(max_length=100, label="Видеокарта", widget=forms.TextInput(attrs={'placeholder': 'RTX 4060...'}))