import React,{useState , useEffect} from 'react';

function Resize(){
    const [width, setWidth] = useState(window.innerWidth);
    const [height, setHeight] = useState(window.innerHeight);

    useEffect(()=>{
        window.addEventListener("resize", handleResize)
        console.log("Event Listenner added")

        return() => {
            window.removeEventListener("resize" , handleResize);
            console.log("Event Listenner removed")
        }
    },[]);

    useEffect(() => {
        document.title  = `Size: ${width} X ${height} `
    },[width, height]);

   

    function handleResize(){
        setWidth(window.innerWidth);
        setHeight(window.innerHeight)
    }
    return(
        <>
        <p>Window Width: {width}px</p>
        <p>Window Heigth: {height}px</p>
        </>
    )
}
export default Resize