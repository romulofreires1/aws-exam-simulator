import type { Metadata } from "next";
import "./globals.css";
import { Header } from "@/components/common/Header";

export const metadata: Metadata = {
  title: "AWS Exam Simulator • Official AWS Certification Simulator",
  description: "AWS certification exam simulator featuring Real and Practice modes, domain performance breakdown, and local storage.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
    apple: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="bg-slate-950 text-slate-100 min-h-screen antialiased selection:bg-amber-500 selection:text-slate-950">
        <Header />
        {children}
      </body>
    </html>
  );
}
