![Cover](https://github.com/karina-anggraeni/Stock-Price-Predictions/blob/main/Sample%20Image/Cover.png)

This project serves as the final and ultimate exam for Purwadhika Data Science and Machine Learning course I have been taking for the past 5 months. I have an interest in stock markets and pricing, that is why I decided to choose this topic. Even though far from perfect, I hope this project can be a stepping stone for me to learn more about data science algorithms in the future. For more details abou this project, you can kindly check my jupyter notebook files under **Stock Predictions - EDA and Modeling** folder.

### **Problem Statement** </br>
Predicting stock prices could be tricky and time-consuming. Generaly, there are two dofferent approach to predicting stock prices. There is _fundamental analysis_ (predicting stock prices based on the company’s financial statement) and _technical analysis_ (predicting stock prices based on its charts and patterns). In this project, I want to focus on using machine learning modeling as a different approach to _technical analysis_ in predicting stock prices using its own historical data.

### **Expected Goal** </br>
We want to predict possible stock prices outcomes or expected trends by fitting its historical data to machine learning algorithms. This approach will be beneficial for traders, investors, fund managers, financial advisors, securities, etc.

### **Dataset** </br>
I am using stock historical data from 6 different banks that I choose from 3 categories. Those are national private bank (BBCA and MEGA), state-owned public bank (BBRI and BMRI) and foreign private bank (SDRA and BNII). I collect the data from Neo HOTS Application by Mirae Asset Securities (for private used only).

### **Insights and Analysis** </br>
I explored each datasets to come with insightful informations about said datasets. For example, I wanted to map how each stock's returns are correlated to one another.

![EDA](https://github.com/karina-anggraeni/Stock-Price-Predictions/blob/main/Sample%20Image/EDA_Example.png)

### **Modeling and Evaluation** </br>
For machine learning modeling, I picked BBCA, BBRI, and BNII to represent each bank category. I used ARIMA and LSTM because their algorithms are well known to give great prediction result to time-series data. To evaluate each model's performance, I used MSE and RMSE evaluation score.

### **Conslusion** </br>
LSTM Model gives the best prediction for each stock; it provides us with low RMSE score and it best mirror stock price's movements. We need to to take notes that this model gives best result when real data is given using a short-term prediction iteration.

![Compare](https://github.com/karina-anggraeni/Stock-Price-Predictions/blob/main/Sample%20Image/BNII_Comparation.png)

When LSTM Model uses its own prediction values repeatedly as an input to predict new values, in the end the stock price will be convergent to a fixed price.

![Predict](https://github.com/karina-anggraeni/Stock-Price-Predictions/blob/main/Sample%20Image/BNII_Prediction.png)

### **Challenges** </br>
Although this model seems to best fit to our data, it needs quite some computational effort for large datasets. Furthermore, the number of layers and parameter used for data training does not follow a specific rule and tuning the parameters is still a trial and error process.

### **Reference** </br>
1. https://www.youtube.com/watch?v=QIUxPv5PJOY
2. https://www.youtube.com/watch?v=gqryqIlvEoM
3. https://towardsdatascience.com/data-analysis-visualization-in-finance-technical-analysis-of-stocks-using-python-269d535598e4
4. https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21#:~:text=An%20LSTM%20has%20a%20similar,operations%20within%20the%20LSTM's%20cells.&text=These%20operations%20are%20used%20to,to%20keep%20or%20forget%20information.
5. https://towardsdatascience.com/choosing-the-right-hyperparameters-for-a-simple-lstm-using-keras-f8e9ed76f046
