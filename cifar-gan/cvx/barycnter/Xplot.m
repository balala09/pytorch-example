function [ ] = Xplot( x,K,w )
%UNTITLED6 �˴���ʾ�йش˺�����ժҪ
%   ���ƾ�������
    for i = 1:K
        if w(i) ~=0
            plot(x(i,1),x(i,2),'b+');
            hold on;
        end
    end   
end

