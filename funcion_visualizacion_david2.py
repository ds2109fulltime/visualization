
def draw_circle(data, column, title):
    ''' This function performs a pie chart with the inner circle blank. When it is to be called
        -dataframe is entered in the "data" attribute,
        -column attribute: enter the column whose two values you want to represent, as a result, will give you the count '''
    import matplotlib.pyplot as plt
    total = data[column].value_counts()
    my_circle=plt.Circle( (0,0), 0.7, color='white') 
    plt.figure(figsize=(10,10))
    plt.pie(total.values,
            labels = total.index,
            autopct='%1.2f%%')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title(title)
    plt.show()
