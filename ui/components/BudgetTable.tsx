import styles from './BudgetTable.module.css';

const budgets = [
  {
    stockName: "ABC Corp",
    pe: "25.4",
    price: "₹500",
    date: "12 Dec 2024",
    listingTime: "10:00 AM",
    marketCap: "500 Cr",
    industryPE: "20.8",
    high: "₹550",
    yearHigh: "₹560",
    low: "₹450",
  },
  {
    stockName: "XYZ Ltd",
    pe: "30.2",
    price: "₹300",
    date: "11 Dec 2024",
    listingTime: "11:00 AM",
    marketCap: "700 Cr",
    industryPE: "22.5",
    high: "₹320",
    yearHigh: "₹330",
    low: "₹280",
  },
  {
    stockName: "PQR Inc",
    pe: "28.9",
    price: "₹400",
    date: "10 Dec 2024",
    listingTime: "9:30 AM",
    marketCap: "600 Cr",
    industryPE: "25.0",
    high: "₹450",
    yearHigh: "₹470",
    low: "₹380",
  },
  {
    stockName: "LMN Co",
    pe: "24.7",
    price: "₹700",
    date: "9 Dec 2024",
    listingTime: "1:00 PM",
    marketCap: "800 Cr",
    industryPE: "23.1",
    high: "₹750",
    yearHigh: "₹780",
    low: "₹650",
  },
  {
    stockName: "DEF Ltd",
    pe: "32.1",
    price: "₹200",
    date: "8 Dec 2024",
    listingTime: "3:00 PM",
    marketCap: "300 Cr",
    industryPE: "19.5",
    high: "₹230",
    yearHigh: "₹240",
    low: "₹190",
  },
  {
    stockName: "GHI Tech",
    pe: "29.3",
    price: "₹1000",
    date: "7 Dec 2024",
    listingTime: "2:00 PM",
    marketCap: "1,200 Cr",
    industryPE: "27.2",
    high: "₹1050",
    yearHigh: "₹1100",
    low: "₹900",
  },
];

export default function BudgetList() {
  return (
    <div className={styles.gridContainer}>
      {budgets.map((budget, index) => (
        <div key={index} className={styles.budgetCard}>
          <table className={styles.table}>
            <thead>
              <tr>
                <th>Stock Details</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Stock Name</td>
                <td>{budget.stockName}</td>
              </tr>
              <tr>
                <td>PE</td>
                <td>{budget.pe}</td>
              </tr>
              <tr>
                <td>Price</td>
                <td>{budget.price}</td>
              </tr>
              <tr>
                <td>Date</td>
                <td>{budget.date}</td>
              </tr>
              <tr>
                <td>Listing Time</td>
                <td>{budget.listingTime}</td>
              </tr>
              <tr>
                <td>Market Cap</td>
                <td>{budget.marketCap}</td>
              </tr>
              <tr>
                <td>Industry PE</td>
                <td>{budget.industryPE}</td>
              </tr>
              <tr>
                <td>High</td>
                <td>{budget.high}</td>
              </tr>
              <tr>
                <td>Year High</td>
                <td>{budget.yearHigh}</td>
              </tr>
              <tr>
                <td>Low</td>
                <td>{budget.low}</td>
              </tr>
            </tbody>
          </table>
          <button className={styles.knowMoreButton}>Know More</button>
        </div>
      ))}
    </div>
  );
}
