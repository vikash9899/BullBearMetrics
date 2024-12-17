import Link from "next/link";
import BudgetTable from '@/components/BudgetTable';
import BudgetLayout from "@/components/BudgetLayout";

export default function Home() {
  return (
    <div>
      Hello World. <Link href="/about">About</Link>
      <h1>Budget Display</h1>
      <BudgetTable/>  
       
    </div>

  );
}

