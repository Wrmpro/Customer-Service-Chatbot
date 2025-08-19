# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'return' in user_input or 'refund' in user_input:
        return "🔄 Our return policy allows returns within 30 days of delivery with a full refund if the item is unused and in original packaging."
    
    elif 'order status' in user_input or 'where is my order' in user_input or 'track order' in user_input:
        return "📦 Please provide your order ID to track the status. You can also track it from your account under 'My Orders'."
    
    elif 'cancel' in user_input:
        return "❌ You can cancel your order within 24 hours of placing it from your account page under 'My Orders'."
    
    elif 'working hours' in user_input or 'open' in user_input or 'timings' in user_input:
        return "🕘 We are open from 9 AM to 6 PM, Monday to Saturday, and closed on public holidays."
    
    elif 'payment options' in user_input or 'payment methods' in user_input:
        return "💳 We accept credit cards, debit cards, net banking, UPI, and cash on delivery for selected locations."
    
    elif 'contact' in user_input or 'customer care' in user_input or 'support' in user_input:
        return "📞 You can contact our customer care at +1-234-567-8901 or email us at support@example.com."
    
    elif 'exchange' in user_input:
        return "🔁 We offer exchange only for damaged or defective items within 7 days of delivery. Please raise a request in your account."

    elif 'shipping charges' in user_input or 'delivery charges' in user_input:
        return "🚚 Shipping is free for orders above $50. For orders below that, a flat $5 delivery charge applies."

    else:
        return "🤖 I'm sorry, I didn't understand your question. Please contact support@example.com for further assistance."
