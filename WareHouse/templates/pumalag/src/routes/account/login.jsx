import { Menu , Popover , Transition  } from '@headlessui/react'
import { usePopper } from 'react-popper'
import {  ChevronRightIcon } from '@heroicons/react/solid'
import {  useState } from 'react'



export default function Login() {
    let [referenceElement, setReferenceElement] = useState()
    let [popperElement, setPopperElement] = useState()
    let { styles, attributes } = usePopper(referenceElement, popperElement,)

  return (
    <Popover >

           <Popover.Button ref={setReferenceElement}>
            <h2>Login</h2>
            
           </Popover.Button>
            

          <Popover.Panel className=" bg-gradient-to-l from-gray-800 px-4 rounded-lg "
            ref={setPopperElement}
            style={styles.popper}
            {...attributes.popper}
            >
                <Transition
                enter="transition duration-800 ease-out"
                enterFrom="transform scale-0 opacity-0"
                enterTo="transform scale-100 opacity-100"
                leave="transition duration-800 ease-out"
                leaveFrom="transform scale-95 opacity-100"
                leaveTo="transform scale-0 opacity-0"
                >

                  <div className="grid py-2 container  ">
    {/*                <input > name email</input>
                    <input> password</input>*/}
awdcawd awda
                  </div>
                </Transition>

          </Popover.Panel>

    </Popover>

  );
}

//how to import// import Login from "./routes/account/login";