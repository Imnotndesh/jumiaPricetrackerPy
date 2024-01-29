# Jumia Price Tracker
![Delivery](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzFoeWYybzNyMXNjd243YTNvMGFtenNhMmcydzM2OWFoY2VidTlkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f8WG3NAyOMFHroIEj0/giphy-downsized.gif)
- A simple python script to check the lowest price for your desired product in JumiaKE website
- It also displays he current price as a desktop notification as below:
  
![Sample Notification](https://github.com/Imnotndesh/jumiaPricetrackerPy/assets/103320083/0d93dea8-c915-4421-bd25-e705de5705d4)

- The script refreshes every 5 minutes but can be easily configured to change the duration
# How to use
- Clone the repository above in your specified directory
- Obtain the full name for the item from the jumia website 
- Open the `main.py` file with your favourite editor
- Edit the `getItems()` funtion so as to include the product name i.e:
```
getItems("Insert full product name here")
```
*PS - I have only tested this on gnome based linux distros
