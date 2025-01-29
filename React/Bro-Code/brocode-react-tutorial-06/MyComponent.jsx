import React,{useState} from 'react';

function MyComponent (){
    const [name , setName] = useState("Guest");
    const [quantaty, setQuantaty] = useState(1);
    const [comment, setComment] = useState();
    const [payment, setPayment] = useState('');
    const [shipping, setShipping] = useState('Delivery');

    function handleShippingChange(event){
        setShipping(event.target.value)
    }

    function handlePaymentChange(event){
        setPayment(event.target.value)
    }

    function handleCommentChange(event){
        setComment(event.target.value)
    }

    function handleQuantatyChange(event){
        setQuantaty(event.target.value)
    }

    function handleNameChange(event){
        setName(event.target.value);
    }
    return(
        <div>
            <input value={name} onChange={handleNameChange}/>
            <p>Name: {name}</p>

            <input value={quantaty} onChange={handleQuantatyChange} type='number'/>
            <p>Quantaty: {quantaty}</p>

            <textarea value={comment} onChange={handleCommentChange} placeholder='Enter Delivery Instructions'/>
            <p>Comment: {comment}</p>

            <select value={payment} onChange={handlePaymentChange}>
                <option value=''>Select an Option</option>
                <option value='Visa'>Visa</option>
                <option value='MasterCard'>MasterCard</option>
                <option value='GiftCard'>GiftCard</option>
            </select>
            <p>Payment: {payment}</p>

            <label>
                <input type='radio' value='Pick Up'  checked={shipping === "Pick Up"} onChange={handleShippingChange}/>
                Pick Up
            </label><br></br>
            
            <label>
                <input type='radio' value='Delivery'  checked={shipping === "Delivery"} onChange={handleShippingChange}/> 
                Delivery
            </label>
            <p>Shipping: {shipping}</p>
        </div>

    )
}
export default MyComponent