import type { Metadata } from "next";
import "./globals.css";
import { Header } from "@/components/common/Header";

export const metadata: Metadata = {
  title: "AWS Exam Simulator • Simulador Oficial de Certificações AWS",
  description: "Simulador de exames e certificações AWS com modo real e treino, métricas por domínio e armazenamento local.",
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
    <html lang="pt-BR" className="dark">
      <body className="bg-slate-950 text-slate-100 min-h-screen antialiased selection:bg-amber-500 selection:text-slate-950">
        <Header />
        {children}
      </body>
    </html>
  );
}
