import { useState, useEffect, useRef } from 'react';
import { MessageSquare, Send, Plus, Upload, User, Bot, Loader2 } from 'lucide-react';

const API_URL = "http://localhost:8000";

export default function App() {
  const [sessions, setSessions] = useState([]);
  const [currentSession, setCurrentSession] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  useEffect(() => { scrollToBottom(); }, [messages, isLoading]);

  useEffect(() => { fetchSessions(); }, []);

  const fetchSessions = async () => {
    try {
      const res = await fetch(`${API_URL}/sessions`);
      const data = await res.json();
      setSessions(data.sessions || []);
      if (data.sessions?.length > 0 && !currentSession) loadHistory(data.sessions[0].id);
      else if (data.sessions?.length === 0) createNewSession();
    } catch (e) { console.error("Lỗi fetch sessions", e); }
  };

  const createNewSession = async () => {
    try {
      const res = await fetch(`${API_URL}/create_session`, { method: 'POST' });
      const data = await res.json();
      setCurrentSession(data.session_id);
      setMessages([]);
      fetchSessions();
    } catch (e) { console.error("Lỗi tạo session", e); }
  };

  const loadHistory = async (sessionId) => {
    setCurrentSession(sessionId);
    try {
      const res = await fetch(`${API_URL}/chat_history/${sessionId}`);
      const data = await res.json();
      setMessages(data.history || []);
    } catch (e) { console.error("Lỗi load history", e); }
  };

  const sendMessage = async (e) => {
    e?.preventDefault();
    if (!input.trim() || !currentSession) return;
    const userMsg = input;
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setIsLoading(true);

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: currentSession, message: userMsg })
      });
      const data = await res.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.answer }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'Lỗi kết nối. Vui lòng thử lại!' }]);
    } finally { setIsLoading(false); }
  };

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    alert("Đang nạp dữ liệu vào AI, vui lòng đợi...");
    try {
      const res = await fetch(`${API_URL}/upload`, { method: 'POST', body: formData });
      const data = await res.json();
      alert(data.message);
    } catch (err) { alert("Lỗi nạp file!"); }
  };

  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      <div className="w-1/4 bg-vinhomes-blue text-white flex flex-col shadow-xl z-10">
        <div className="p-5 border-b border-blue-800">
          <h1 className="text-2xl font-bold text-vinhomes-gold tracking-wide">VinHomes AI</h1>
          <p className="text-sm text-gray-300 mt-1">Trợ lý Kinh doanh Cấp cao</p>
        </div>
        <div className="p-4">
          <button onClick={createNewSession} className="w-full flex items-center justify-center gap-2 bg-vinhomes-gold hover:bg-yellow-600 text-blue-900 font-bold py-3 rounded-lg transition-all">
            <Plus size={20} /> Tư vấn khách hàng mới
          </button>
        </div>
        <div className="flex-1 overflow-y-auto px-3 space-y-2">
          {sessions.map(s => (
            <button key={s.id} onClick={() => loadHistory(s.id)} className={`w-full text-left p-3 rounded-lg flex items-center gap-3 transition-colors ${currentSession === s.id ? 'bg-blue-800 border-l-4 border-vinhomes-gold' : 'hover:bg-blue-900'}`}>
              <MessageSquare size={18} className={currentSession === s.id ? 'text-vinhomes-gold' : 'text-gray-400'} />
              <span className="truncate text-sm">{s.title || "Tư vấn mua nhà mới"}</span>
            </button>
          ))}
        </div>
        <div className="p-4 border-t border-blue-800 text-center">
          <label className="cursor-pointer text-xs text-gray-400 hover:text-white flex justify-center items-center gap-1">
            <Upload size={14} /> Nạp Data (CSV)
            <input type="file" accept=".csv" className="hidden" onChange={handleFileUpload} />
          </label>
        </div>
      </div>
      <div className="w-3/4 flex flex-col bg-white">
        <div className="flex-1 overflow-y-auto p-8 space-y-6">
          {messages.length === 0 && (
            <div className="h-full flex flex-col items-center justify-center text-gray-400">
              <Bot size={64} className="text-vinhomes-blue mb-4 opacity-20" />
              <p>Hãy bắt đầu. Ví dụ: "Tìm căn 3PN ở Hoàng Mai"</p>
            </div>
          )}
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex gap-4 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              {msg.role === 'assistant' && (
                <div className="w-10 h-10 rounded-full bg-vinhomes-blue flex items-center justify-center shadow-md flex-shrink-0"><Bot size={20} className="text-vinhomes-gold" /></div>
              )}
              <div className={`max-w-[70%] p-4 rounded-2xl shadow-sm whitespace-pre-wrap ${msg.role === 'user' ? 'bg-blue-100 text-blue-900 rounded-tr-none' : 'bg-white border border-gray-200 text-gray-700 rounded-tl-none'}`}>
                {msg.content}
              </div>
              {msg.role === 'user' && (
                <div className="w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center shadow-md flex-shrink-0"><User size={20} className="text-gray-600" /></div>
              )}
            </div>
          ))}
          {isLoading && (
            <div className="flex gap-4 justify-start">
              <div className="w-10 h-10 rounded-full bg-vinhomes-blue flex items-center justify-center"><Bot size={20} className="text-vinhomes-gold" /></div>
              <div className="bg-white border border-gray-100 p-4 rounded-2xl rounded-tl-none flex items-center gap-2 text-gray-500">
                <Loader2 className="animate-spin" size={16} /> AI đang phân tích giỏ hàng...
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
        <div className="p-6 bg-white border-t border-gray-100">
          <form onSubmit={sendMessage} className="flex gap-3 relative">
            <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Nhập yêu cầu tìm kiếm nhà..." className="flex-1 p-4 pr-16 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-vinhomes-blue" disabled={isLoading} />
            <button type="submit" disabled={isLoading || !input.trim()} className="absolute right-2 top-2 bottom-2 aspect-square bg-vinhomes-gold hover:bg-yellow-600 text-white rounded-lg flex items-center justify-center disabled:opacity-50"><Send size={20} /></button>
          </form>
        </div>
      </div>
    </div>
  );
}