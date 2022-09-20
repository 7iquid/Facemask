import React, { useState } from 'react'

import './tailwind.css';



export default function Menu() {

  // useEffect(() => {
  //       let sidebar = document.querySelector('.pop')
  //       sidebar.classList.toggle("-translate-x-full");
  //   }
  

  // sidebar

  return (
    <ul className='flex justify-end py-4 absolute'>
      <li className='px-2'>Home</li>
      <li className='px-2'>Login</li>
      <li className='px-2'>About</li>
    </ul> 
  );
}